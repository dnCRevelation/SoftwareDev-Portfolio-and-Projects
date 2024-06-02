import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Project {
    title: string;
    description: string;
    image: string;
}

@Injectable({
    providedIn: 'root'
})
export class ProjectService {
    private apiUrl = 'http://127.0.0.1:8000/api/projects/';

    constructor(private http: HttpClient) { }

    getProjects(): Observable<Project[]> {
        return this.http.get<Project[]>(this.apiUrl);
    }
}