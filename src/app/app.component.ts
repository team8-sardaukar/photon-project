import { Component, OnInit, OnDestroy } from '@angular/core';
import { PlayersDBService } from './players/players-DB.service';
import { Player } from './players/player.model';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';

/* This component implements the splash screen, and also
 * is the background that the rest of the pages
 * will be rendered on top of.
 */


/*  The stuff commented out in this file will prevent
 *  the front end from compiling because it can't pull
 * the data from the database.
 */

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit/*, OnDestroy*/ {
  title = 'frontend';
  playersListSubs = Subscription;
  //playersList: Player[];

  constructor (private playersDB: PlayersDBService, 
    private router: Router)
  {

  }

  ngOnInit() 
  {
    //Redirect to player entry screen after 3 seconds on splash
    setTimeout(() => {
      this.router.navigate(['/player-entry']);
    }, 3000);
  }

  ngOnDestroy() 
  {
    //this.playersListSubs.unsubscribe();
  }
}