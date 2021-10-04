import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import * as React from 'react';

@Component({
  selector: 'app-player-entry',
  templateUrl: './player-entry.component.html',
  styleUrls: ['./player-entry.component.css']
})
export class PlayerEntryComponent implements OnInit{

  constructor(
    private route: ActivatedRoute,
  ) { 

  }

  ngOnInit(): void {
  }

}
