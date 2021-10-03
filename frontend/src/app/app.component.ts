import { Component, OnInit, OnDestroy } from '@angular/core';
import { PlayersDBService } from './players/players-DB.service';
import { Player } from './players/player.model';
import { Subscription } from 'rxjs';

/*  The stuff commented out in this file will prevent
 *  the front end from compiling because it can't pull
 * the data from the database.
 */

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent /*implements OnInit, OnDestroy*/ {
  title = 'frontend';
  playersListSubs = Subscription;
  //playersList: Player[];

  constructor (private playersDB: PlayersDBService)
  {

  }

  ngOnInit() 
  {
  /*  this.playersListSubs = this.playersDB
    
    .getPlayers()
    .subscribe(res => 
      {
        this.playersList = res;
      },
      console.error);
      */
  }

  ngOnDestroy() 
  {
    //this.playersListSubs.unsubscribe();
  }
}