import React, { useEffect, useState } from 'react';
import { getProjects } from '../services/projectService';

const Projects = () => {
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        const fetchProjects = async () => {
            const data = await getProjects();
            setProjects(data);
        };

        fetchProjects();
    }, []);

    return (
        <div className="projects-container">
            {projects.map(project => (
                <div key={project.id} className="project-card">
                    <img src={project.image} alt={project.title} />
                    <h3>{project.title}</h3>
                    <p>{project.description}</p>
                </div>
            ))}
        </div>
    );
};

export default Projects;
