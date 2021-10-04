import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PlayerEntryComponent } from './player-entry/player-entry.component';

const routes: Routes = [
  { path: 'player-entry', component: PlayerEntryComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
