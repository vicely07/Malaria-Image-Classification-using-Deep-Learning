# Malaria-Image-Classification-using-Deep-Learning
A project for HackHouston 2019 

##Team
Vi Ly: Deep Learning
Cuong Pham: Transfer Learning
 Nguyen Phan: Web Designing

## Inspiration
The deadly disease has reached epidemic, even endemic proportions in different parts of the world — killing around 400,000 people annually. In other areas of the world, it’s virtually nonexistent. Some areas are just particularly prone to a disease outbreak — there are certain factors that make an area more likely to be infected by malaria:
High poverty levels
Lack of access to proper healthcare
Political instability
Presence of disease transmission vectors (ex. mosquitos)

## What it does
We want to create a web-based service powered that can classify accurately the skin cell with sign of Malaria. 

Current diagnosing methods of this disease are tedious and time-consuming.


## How we built it
1. We first created a deep learning model from Keras package (with Tensorflow backend). The model consists of 3 convolutional layers and 2 dense layers.

2. We trained 13780 Malaria infected and 13780 uninfected images on our deep learning framework. 80% are used for training and 20% are used for testing. The best model was saved in form of an .h5 file.

3. We imported the .h5 model to website using Flask.

4. We add more functions to the web service, added a logo and changed the color theme/graphics. 

## Challenges I ran into
With this mixture of these problems, we must keep some things in mind when building our model:
There may be a lack of a reliable power source
Battery-powered devices have less computational power
There may be a lack of Internet connection (so training/storing on the cloud may be hard!)
While we want to obtain the highest level of accuracy as possible, we must also consider making the model as small and computationally efficient as possible — and also able to be deployed to edge and Internet of Things devices.

## Accomplishments that I'm proud of
We are proud that this free web service can be used to aid in the early detection of Malaria. This can help to save the cost of healthcare and the problem of short-staffing at medical facility in many developing countries. 

## What we learned
We learned to work under pressure and create a finished web service product in the limited timeframe of 24 hour.

## What's next for Malaria Scanner
We will further develop the deep learning model so that it can count infected blood cells from smear slide images, which lead to a more guaranteed result of Malaria detection.
