---
title: Should Models Be Accurate?
date: '2022-06-09'
type: page
weight: 30
highlight: true
---

Contributed Talk at RLDM 2022. [Watch here](https://brown.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=fcc5c7d6-9307-45c3-b05b-aea800ef8460&start=6083.618718).

<!--more-->
## Abstract

Model-based Reinforcement Learning (MBRL) holds promise for data-efficiency by planning with model-generated experience in addition to learning with experience from the environment. However, in complex or changing environments, models in MBRL will inevitably be imperfect, and their detrimental effects on learning can be difficult to mitigate. In this work, we question whether the objective of these models should be the accurate simulation of environment dynamics at all. We focus our investigations on Dyna-style planning in a prediction setting. First, we highlight and support three motivating points: a perfectly accurate model of environment dynamics is not practically achievable, is not necessary, and is not always the most useful anyways. Second, we introduce a meta-learning algorithm for training models with a focus on their usefulness to the learner instead of their accuracy in modelling the environment. Our experiments show that in a simple non-stationary environment, our algorithm enables faster learning than even using an accurate model built with domain-specific knowledge of the non-stationarity. 

