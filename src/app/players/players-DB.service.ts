import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BACKEND_URL } from '../env';
import { Player } from './player.model';

@Injectable()

export class PlayersDBService 
{
    constructor (private http: HttpClient)
    {

    }

    // Consider implementing error handling in service here

    getPlayers(): Observable<Player[]>
    {
        return this.http
            .get<Player[]>(`${BACKEND_URL}/players`)
            //Call error handler with .catch
    }
}