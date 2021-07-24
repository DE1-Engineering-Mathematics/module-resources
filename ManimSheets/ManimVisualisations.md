# Manim Visualisations

![Logo](gettingStarted\media\logo.png)
## Getting Started

Manim is an open source Python Library developed by [3Blue1Brown](https://www.youtube.com/c/3blue1brown) for creating visually explanatory maths videos. These animations are done programmatically, and the script is rendered to produce a video. 

This offers some key advantages. Programming logic such as loops are available to create very powerful results. Prebuilt scripts can be tailored to concepts or questions on the course, and the animations can be played around with to see how different inputs behave.

### Installation
There are two versions of Manim: [3Blue1Brown's personal version](https://github.com/3b1b/manim), and a [community edition](https://github.com/ManimCommunity/manim). Using the latter is preferred as it is more stable and better documented. 

As a prerequisite, Python should already be set up in Computing 1. The installation instructions are relatively straight forward, and can be found [here](https://docs.manim.community/en/stable/installation.html) for your relevant platform. The scripts were created in and are compatible with Manim Community v0.8.0.

### Usage
#### Rendering Prebuilt Scripts
If using one of the prebuilt visualisation scripts, copy the text into VS Code or your preferred text editor, and save the file as per the comment at the top e.g. `vectors.py`. Open a Terminal at the location of this file, and the manim command can be used to render the script into a video:

```
manim -pqh filename.py Scene
```

* Replacing `qh` with `ql` will output a low resolution and low framerate video, useful for rapid prototyping.
* Ensure the `filename` corresponds to the file with that was copied and saved earlier
* The topic file groups multiple scenes denoted by each Python class e.g. `DotProduct`, `CrossProduct`. Changing this will render different visualisations withing the same topic

An example, for the vectors script would be:
```
manim -pqh linear_transform.py R3
```
And this will open:
<style> 
  video {
    width: 720px;
    height: 480px;
    display: block;
    margin: 0 auto;
</style>  
<video controls>
  <source src="gettingStarted\media\R3.mp4" type="video/mp4">
</video>
<br />

#### Editing Prebuilt Scripts
To see how different inputs behave, the top of the prebuilt script contains comments on how to edit these defaults. The script must be rendered again to produce a video that overwrites the previous.

For more information, the Manim Community Documentation is really useful. Have a go at writing your own scripts! 
* [Tutorials](https://docs.manim.community/en/stable/tutorials.html) 
* [Example Gallery](https://docs.manim.community/en/stable/examples.html)
* [Reference Manual](https://docs.manim.community/en/stable/reference.html)

## Engineering Mathematics Topics - Term 1
- [2. Vectors](./Topics_term1/2_Vectors.md)
- [4A. Linear Transformations](./Topics_term1/4A_Linear_Trans.md)
- [6. Complex Numbers](./Topics_term1/6_Complex_num.md)


###### Dyson School of Design Engineering 2021 - Cosmin Vonsovici
###### For any mistakes or queries please do not hesitate to email me at cav20@ic.ac.uk
