#!/usr/bin/env python
# coding: utf-8

# # Find the max using PSO

# # Maryam Hoseeinali 610398209

# ## general explanation:

# ### In this implementation maximum of given function is calculated based on the particle swarm optimization (PSO).

# In[ ]:





# ## import required libraries

# In[17]:


import math
import random


# ## fitness function:
# ### this function defines the objective function f(x,y) that we want to optimize it. which is calculated in several parts to prevent mistakes.

# In[18]:


def f(x, y):
    pi = math.pi
    f1 = (math.sin(x))*(math.cos(y))
    f2 = math.exp(abs(1-(math.sqrt((x**2+y**2)))/pi))
    z = abs(f1*f2)
    return z
    


# ## Particle Class:
# ## particle class represent an individual particle in PSO algorithm.
# 
# ## initialization:
# ### the __init__ method initializes the particle's best position and velocity randomly and sets the particle's best position and best fitness to its current position and fitness.
# ### - x and y represent current position of the particle in the search space.
# ### - vx and vy represent the current velocity of the particle in the x and y directions.
# ### - best_x and best_y stores the best position the particle has ever found during the optimization process.
# ### - best_fitness stores the fitness value associated with the best position found by particle.
# 
# ## update_velocity method:
# ### - the update_velocity method updates the particle's velocity based on its current velocity, its best position and the global best position.
# ### - w, cognitive_c and social_c are hyperparameters of PSO algorithm that control the particle's movement.
# ### - w is the inertia weight that determines the influence of the particle's previous velocity on its current velocity.
# ### - higher value of w gives more weight to the particle's previous velocity.
# ### - lower value of w gives more weight to the social and cognitive components.
# ### - cognitive_c and social_c are the learning factors that control the influence of the particle's best position and the global best position on its velocity update.
# ### - higher value of cognitive_c gives more weight to the particle's best position
# ### - higher value of social_c gives more weight to the global best position.
# ### - by adjusting the values of cognitive_c, social_c and w we control the balance between exploration and exploitation.
# 
# ## update_position method:
# ### update_position method updates the position of a particle based on its velocity, consider boundary constraints and updates the particle's best position and fitness value if an improvement is achieved.this process allows the particle to explore the search.

# In[ ]:


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.best_x = x
        self.best_y = y
        self.best_fitness = f(x, y)

    def update_velocity(self, global_best_x, global_best_y, w, cognitive_c, social_c):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        self.vx = w*self.vx + cognitive_c*r1*(self.best_x - self.x) + social_c*r2*(global_best_x - self.x)
        self.vy = w*self.vy + cognitive_c*r1*(self.best_y - self.y) + social_c*r2*(global_best_y - self.y)
## based on original velocity update equation from lecture4

    def update_position(self,min_xy, max_xy):
        self.x += self.vx
        self.y += self.vy
## position update (after updating velocity in previous method)     
        
        
        
        if self.x < min_xy:
            self.x = min_xy
            self.vx *= -1
        elif self.x > max_xy:
            self.x = max_xy
            self.vx *= -1
        if self.y < min_xy:
            self.y = min_xy
            self.vy *= -1
        elif self.y > max_xy:
            self.y = max_xy
            self.vy *= -1
##boundry constraints
## the method checks if the particle's position violates the specified boundry constrants
## if the particle's position exceeds the boundaries, it is adjusted to the nearest boundry
## value and thecorresponding velocity component is reversed to simulate bouncing off the boundry.
            
            
            
            
        fitness = f(self.x, self.y)
        if fitness > self.best_fitness:
            self.best_x = self.x
            self.best_y = self.y
            self.best_fitness = fitness
            
            
## fitness update
## the method calculates the fitness value of the updated position
## and compares it with the particle's previous best fitness value
## particle's best position and best fitness will be updated after comparison if needed.


# In[ ]:


## particle swarm optimization
### particle swarm optimization function implements the PSO algorithm to search for the global maximum of a function in given search space.


# In[20]:


def particle_swarm_optimization(num_particles, max_iterations, w, cognitive_c, social_c,min_xy, max_xy):
    
    particles = [Particle(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(num_particles)]
## initializes a list of num_particles(the number of particles in the swarm) particles with random positions.
    global_best_x = particles[0].x
    global_best_y = particles[0].y
    global_best_fitness = particles[0].best_fitness
    
    
    for i in range(max_iterations):
#optimization loop

        for particle in particles:
#particle updates
            particle.update_velocity(global_best_x, global_best_y, w, cognitive_c, social_c)
            particle.update_position(min_xy, max_xy)
            if particle.best_fitness > global_best_fitness:
                global_best_x = particle.best_x
                global_best_y = particle.best_y
                global_best_fitness = particle.best_fitness
        print("Best solution so far: = {}".format(global_best_fitness))

    print("\nGlobal best x = {}\nGlobal best y = {}\nGlobal best fitness = {}".format(global_best_x, global_best_y, global_best_fitness))


# In[25]:


particle_swarm_optimization(num_particles=100, max_iterations=20, w=0.5, cognitive_c=1.5, social_c=1.5, min_xy = -10, max_xy = 10)


# In[ ]:




