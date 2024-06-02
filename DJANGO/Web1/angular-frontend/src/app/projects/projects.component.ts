
import { Component, OnInit } from '@angular/core';
import { ProjectService } from '../project.service';

@Component({
    selector: 'app-projects',
    templateUrl: './projects.component.html',
    styleUrls: ['./projects.component.css']
})
export class ProjectsComponent implements OnInit {
    projects = [];

    constructor(private projectService: ProjectService) { }

    ngOnInit(): void {
        this.projectService.getProjects().subscribe(data => {
            this.projects = data;
        });
    }
}
