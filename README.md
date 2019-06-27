# **Project Name: Self-driving Car Simulator**

## **Purpose**:
   The purpose of this project is creating a simulator framework to help testing autopilot software

## **Concepts**:
   This simulator is going to simulate real world traffic scenarios with trained nuronal networks. There are going to have **front end GUI** (build by Unity3D), **back end controller** (test autopilot software). Detail design please check [Simulator Design Concept](#Simulator-Design-Concepts)

## **Simulate Scenarios**:
   ### 1. Parking:
   * **1-1.** System will generate a random parking map, holes, vechicles, and pedestrians by the Parking Simulator Nuronal Network:
     * **PASS** standard:
       * Not hitting vechicles
       * Not hitting pedestrians
       * Not hitting walls
       * Not dropping to holes
       * Successfully detected available parking space
       * Successfully parking to empty space

## **Simulator Design Concepts**:
   ### Parking Simulator Nuronal Network:
   * **Component**:
     * **Map Generator**: fectch pre-build maps from database, and created maps can be uploaded/downloaded to/from database. Maps can be randomly picked by the Map Generator or be manually picked by tester.
     * **Vechicle Generator**: multiple Vechicles will be generated randomly with 2 types of states: **Parking** state and **Driving** state:
       * **Parking** state: Vechicles are pakring at parking lots properly (taken 1 space) or inproperly (taken 2 or more space)
       * **Driving** state: Simulating Vechicles driving with: 1 unified installed test autopilot software, 2 with different autopilot sofware installed (could be building autopilot software or third party autopilot software)
     * **Pedestrians Generator**: