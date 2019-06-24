# Project Name: Self-driving Car Simulator

## Purpose:
The purpose of this project is creating a simulator framework to help testing autopilot software

## Concepts:
This simulator is going to simulate real world traffic scenarios with trained nuronal networks. There are going to have **front end GUI** (build by Unity3D), **back end controller** (testing autopilot testing software). Detail design please check [Simulator Design Concept](#Simulator-Design-Concept)

## Simulate Scenarios:
### 1. Parking:
* **1-1.** System will generate a random parking map, holes, vechicles, and pedestrians by the Parking Simulator Nuronal Network:
  * **PASS** standard:
    * Not hitting vechicles
    * Not hitting pedestrians
    * Not hitting walls
    * Not dropping to holes
    * Successfully detected available parking space
    * Successfully parking to empty space


## Simulator Design Concept:
### Parking Simulator Nuronal Network:
* **Component**:
  * **Map Generator**: 


