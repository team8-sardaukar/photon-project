import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-player-entry',
  templateUrl: './player-entry.component.html',
  styleUrls: ['./player-entry.component.css']
})
export class PlayerEntryComponent implements OnInit {

  constructor(
    private route: ActivatedRoute
  ) {  }

  ngOnInit(): void {
  }

}