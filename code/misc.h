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
// *File Name: method.h
//
// *Module Description:
//                      Implementation of uitility functions needed.
//
// *Author(s):
//              - xyz 
//
//----------------------------------------------------------------------------
// $Rev: 2.1 $
// $LastChangedBy: xyz $
// $LastChangedDate: xx/xx/xx $
//----------------------------------------------------------------------------
#include <iostream>
#include <vector>
#include <stdio.h>
#include<stdlib.h>
#include <string>
#include<fstream>
#include <sstream>

#include "method.h"
#include "NN.h"
#include "definitions.h"

using namespace std;

vector <layer> oSlalom (ifstream* infile, NN NNnetw); 
double oSlalomCompute (method Sla, NN NNnetw, int netwSize);

vector<layer> methodInitialization(ifstream* infile, NN NNnetw)
{
	// manual:
	vector<layer> net; 
	for (int i=0; i<NNnetw.net.size(); i++)
	{
		net.push_back(layer());
		net[i].layer_type = NNnetw.net[i].layer_type;
		net[i].compute_type = 1;
		net[i].movement = 0;
		net[i].para_factor = 1;
	} 
	// --------------------
	// config file baed: 
	/*
	*/
	return net;
}

NN VGGInitialization(NN VGG16)
{
	NNlayer lili; 
	
	//First
	lili.layer_type = LI;
	lili.dim = 3000;
	VGG16.addLayer(lili);

	//Second
	lili.layer_type = NL;
	lili.dim = 1000;
	VGG16.addLayer(lili);

	//
	lili.layer_type = LI;
	lili.dim = 3000;
	VGG16.addLayer(lili);

	//
	lili.layer_type = NL;
	lili.dim = 1000;
	VGG16.addLayer(lili);

	//
	lili.layer_type = LI;
	lili.dim = 500;
	VGG16.addLayer(lili);
	
	//
	lili.layer_type = NL;
	lili.dim = 1000;
	VGG16.addLayer(lili);

	//
	lili.layer_type = LI;
	lili.dim = 500;
	VGG16.addLayer(lili);
	//
	lili.layer_type = NL;
	lili.dim = 1000;
	VGG16.addLayer(lili);

	//
	lili.layer_type = LI;
	lili.dim = 500;
	VGG16.addLayer(lili);

	//
	lili.layer_type = NL;
	lili.dim = 1000;
	VGG16.addLayer(lili);

	//
	lili.layer_type = LI;
	lili.dim = 200;
	VGG16.addLayer(lili);

	//
	lili.layer_type = NL;
	lili.dim = 100;
	VGG16.addLayer(lili);

	return VGG16;

}

NN ResInitialization(NN Res)
{
	NNlayer lili; 
	
	//First
	lili.layer_type = LI;
	lili.dim = 200;
	Res.addLayer(lili);

	//Second
	lili.layer_type = LI;
	lili.dim = 100;
	Res.addLayer(lili);

	return Res; 

}