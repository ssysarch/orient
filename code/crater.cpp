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
// *File Name: crater.cpp
//
// *Module Description:
//                     Our implementation of Craterlake paper.  
//
// *Author(s):
//              - xyz 
//
//----------------------------------------------------------------------------
// $Rev: 2.1 $
// $LastChangedBy: xyz $
// $LastChangedDate: xx/xx/xx $
//----------------------------------------------------------------------------
#include "definitions.h"
#include "NN.h"
#include "method.h"
#include <vector>
#include<cmath>


vector <layer> oCrater (ifstream* infile, NN NNnetw)
{
	int netwSize = NNnetw.net.size(); 
	int prect = 100; 
	vector <layer> PPML;

	for (int i=0; i<netwSize; i++)
	{
		PPML.push_back(layer());
		PPML[i].layer_type = NNnetw.net[i].layer_type; 
	}

	//int part1= floor(1 * netwSize); 
	for (int i=0; i<netwSize; i++)
	{
		if(PPML[i].layer_type == LI)
			PPML[i].compute_type = accl; 
		else PPML[i].compute_type = accl; 
		PPML[i].movement = local*1.5;
		PPML[i].para_factor = 1;
	}
	PPML[0].movement = 2*SoC;
	return PPML; 
}

double oCraterCompute (method Sla, NN NNnetw, int netwSize)
{
	double etelatency = 0; // in ms

	//init
	etelatency += dTRANSFER; 
	//etelatency += dTEEinit;

	for (int i =0; i<netwSize; i++)
	{
		etelatency += (NNnetw.net[i].dim / computation[Sla.net[i].compute_type])/Sla.net[i].para_factor;
		etelatency += networking[Sla.net[i].movement]/Sla.net[i].para_factor; 
	} 
	return etelatency; 
}