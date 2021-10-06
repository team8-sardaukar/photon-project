import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PlayersDBService } from './players/players-DB.service';
import { PlayerEntryComponent } from './player-entry/player-entry.component'

@NgModule({
  declarations: [
    AppComponent,
    PlayerEntryComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule
  ],
  providers: [PlayersDBService],
  bootstrap: [AppComponent]
})
export class AppModule { }
