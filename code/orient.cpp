/*
//----------------------------------------------------------------------------
// Copyright (C) 2023 , XYZ
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions
// are met:
//     * Redistributions of source code must retain the above copyright
//       notice, this list of conditions and the following disclaimer.
//     * Redistributions in binary form must reproduce the above copyright
//       notice, this list of conditions and the following disclaimer in the
//       documentation and/or other materials provided with the distribution.
//     * Neither the name of the authors nor the names of its contributors
//       may be used to endorse or promote products derived from this software
//       without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
// OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
// THE POSSIBILITY OF SUCH DAMAGE
//
//----------------------------------------------------------------------------
//
// *File Name: orient.c
//
// *Module Description:
//                       Main Function for Orient Design
//
// *Author(s):
//              - xyz 
//
//----------------------------------------------------------------------------
// $Rev: 1 $
// $LastChangedBy: xyz $
// $LastChangedDate: xx/xx/xx $
//----------------------------------------------------------------------------
*/

#include "definitions.h"
#include "NN.h"
#include "method.h"
#include "misc.h"

#include <iostream>
#include <bitset>
#include <stdio.h>
#include<stdlib.h>
#include <string>
#include<fstream>
#include <sstream>
using namespace std;



/*
We need to add the followings:	Occulemency, Slalom, Origami, CraterLake, Orient with Baseline (TEE, CraterLake)
*/

vector <layer> oSlalom (ifstream* infile, NN NNnetw); 
double oSlalomCompute (method Sla, NN NNnetw, int netwSize);

vector <layer> oOcclu (ifstream* infile, NN NNnetw); 
vector <layer> oTEE (ifstream* infile, NN NNnetw); 
double oOccluCompute (method Sla, NN NNnetw, int netwSize);

vector <layer> oOrigami (ifstream* infile, NN NNnetw); 
double oOrigamiCompute (method Sla, NN NNnetw, int netwSize);

vector <layer> oCrater (ifstream* infile, NN NNnetw); 
double oCraterCompute (method Sla, NN NNnetw, int netwSize);

vector <layer> oOrientT (ifstream* infile, NN NNnetw); 
double oOrientTCompute (method Sla, NN NNnetw, int netwSize);
vector <layer> oOrientC (ifstream* infile, NN NNnetw); 
double oOrientCCompute (method Sla, NN NNnetw, int netwSize);

int main(int argc, char* argv[])
{


	if (argc < 2) { 
		cout << "No config file found. Exiting...";
		return -1;
	}

	ifstream infile(argv[1]); //open the file
	if (!(infile.is_open() && infile.good())) {
		cout<<"error opening the config file\n";
		return -1; 
	}
	// string line; 
	// int i = 0;
	// while (infile) {
	// 		infile>>line;
	// 		stringstream line2(line);
	// 		int x; 
	// 		line2>>x;
	// 		instMem[i] = bitset<8>(x);
	// 		i++;
	// 	}
	NN VGG16;
	NN Resnet;
	VGG16 = VGGInitialization(VGG16); 
	int VGG16_size = VGG16.net.size(); 

	Resnet = ResInitialization(Resnet); 
	int Resnet_size = Resnet.net.size(); 

	vector <layer> PPML;
	PPML = oSlalom (&infile, VGG16);
	method Slalom (PPML, VGG16_size); 

	PPML = oOcclu (&infile, VGG16);
	method Occlumency (PPML, VGG16_size); 
	PPML = oTEE (&infile, VGG16);
	method TEE (PPML, VGG16_size);

	PPML = oOrigami (&infile, VGG16);
	method Origami (PPML, VGG16_size); 

	PPML = oCrater (&infile, VGG16);
	method Crater (PPML, VGG16_size); 

	PPML = oOrientT (&infile, VGG16);
	method oOrientT (PPML, VGG16_size);

	PPML = oOrientC (&infile, VGG16);
	method oOrientC (PPML, VGG16_size);
	//method Occulemency = methodInitialization(&infile, VGG16);
	//vector <layer> Slalom = methodInitialization(&infile, Resnet);

	double etelatency[10];
	int counter = 0 ; 
	etelatency[2]= oSlalomCompute (Slalom, VGG16, VGG16_size); counter++;
	etelatency[1]= oOccluCompute (Occlumency, VGG16, VGG16_size); counter++;
	etelatency[0]= oOccluCompute (TEE, VGG16, VGG16_size); counter++;
	etelatency[3]= oOrigamiCompute (Origami, VGG16, VGG16_size); counter++;
	etelatency[4]= oCraterCompute (Crater, VGG16, VGG16_size); counter++;
	etelatency[5]= oOrientTCompute (oOrientT, VGG16, VGG16_size); counter++;
	etelatency[6]= oOrientCCompute (oOrientC, VGG16, VGG16_size); counter++;

	int baseline = 50; 
	cout << baseline <<endl;
	for(int i=0; i<counter; i++){
		cout<< etelatency[i]<< endl;
	}
	
	return 0;

}