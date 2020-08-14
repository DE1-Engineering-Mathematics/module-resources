# How to make/edit tutorial sheets
This document should give a semi-brief (hopefully) intro to how to start creating and editing the tutorial sheets as well as other math documents in this repository. Assumes minimal knowledge of markdown, LaTeX, GitHub etc.

## Quick edits
GitHub supports on-site editing of all text files, however the preview will not function so it is only useful for very quick edits. With any markdown file opened, click the pencil on the top right.

![Disable security](media\how-to_github-edit.PNG)

# Setting up the full dev environment
If you already have VS Code (or an editor of your choice) and GitHub setup, you can skip pretty much all of this except: "Getting the VS Code preview to display math and other embeds".

## Recommended software: VS Code and GitHub Desktop
[Visual Studio Code](https://code.visualstudio.com/) is a wonderful free code editor that supports markdown previews (and does much, much more).

[GitHub desktop](https://desktop.github.com/) is a great way to interface with GitHub if you don't want to mess around with the command line.

## (GitHub setup) Clone the repository
From the [GitHub repository site](https://github.com/DE1-Engineering-Mathematics/module-resources), click the _"open with github desktop"_ option on green code/clone button and follow the resulting prompts.

![Disable security](media\how-to_clone-github.PNG)

### Never work out of the master branch!!
For a verity of valid reasons, a good Git/GitHub rule is to never work out of your master branch (the main one in this case being all edits to the master branch get published directly to the GitHub pages website). It's good practice to switch to a specific branch or create a new one after cloning. Use the `tutorial-sheets` branch if you do not want to make a new branch for your edits.

![Switch github branch](media\how-to_switch-branch.PNG)

### Other resources
[GitHub Guides: Hello world](https://guides.github.com/activities/hello-world/)

[GitHub Guides: GitHub flow](https://guides.github.com/introduction/flow/)

## (VS Code setup) Setting up the markdown preview
### Spell check and GitHub markdown plugins
Two very useful plugins are
* [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) (pretty self explanatory)
* [Markdown Preview Github Styling](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles) (Uses GitHub's markdown styling)

### Getting the VS code preview to display math and other embeds
By default, the VS Code will not render math/other embedded content. It will not load an external sources for safety reasons, but as long as you don't open any malicious markdown content there is no need for concern.
![Content disabled error](media\how-to_content-disabled.PNG)

#### Step 1, change preview security settings (top right)
![Content disabled error](media\how-to_change-security.PNG)

#### Step 2, disable preview security
![Disable security](media\how-to_disable-security.PNG)

___Warning: Now that we have disabled preview security, make sure you trust all the markdown files you open, as well as their content's sources.___
_(aka: don't forget you left this setting off and then go open up some random file off the internet)_

<br><br>

-----------------------------------------------------------------------------
<br><br>


# Basic markdown and LaTeX
Now that you have access to edit and preview the documents the next thing is to understand what's in them and how they are layed out.

## Quick intro to markdown
The tutorial sheets (and other documents, such as this one) are written as markdown documents. Markdown is essentially a highly optimized way of writing html that contains all the basic formatting options necessary to write static pages. Any `.md` will be rendered on GitHub as markdown.

### Basic markdown syntax
The basic bits of markdown syntax that are useful to know are:

```markdown
# Headings
## Smaller headings
### Even smaller... and so on

[this is a link!](https://imperial.ac.uk/)
![this is an image](tutorial_sheets/00-test-media/cover.png)

* this is the first item in a list
* this is the second item in the list

-------------------------------------------
^ This is a horizontal separator (anything after 3 dashes works)

<br>
^ This is a line break
```

For a full intro, check out [GitHub's guide on how to write markdown](https://guides.github.com/features/mastering-markdown/)

## Quick intro to LaTeX
[LaTeX](https://www.latex-project.org/) is a typesetting language that is specificity designed for scientific and technical documents. It has wonderful math typesetting features that are used in the tutorial sheets to generate pretty looking formulas etc.

### Basic LaTeX syntax
In our pages, any text that is surrounded by $ $ will be rendered using LaTeX (specifically the [MathJax](https://www.mathjax.org/) library). The important bits of LaTeX syntax to know are:

```markdown
$ x^2 $ - Exponents (superscripts)
$ x_1 $ - Subscripts
$ \frac{x}{y} $ - Fractions
$ \Rightarrow $ - Looks like: =>
$ \text{text} $ - Renders anything inside the {} as text, not math
$ \int_{a}^b $ - Integral notation (replace with \sum for sum notation)
$ \quad $ - 4 spaces (used frequently in the original tutorial sheet notation)
$ \space $ - Yep, literally a space (also can use "\ ")
```

https://arachnoid.com/latex/

# Tutorial sheet structure
Tutorial sheets have an opening section with: Learning targets, Reading, Lectures and Additional resources. These are meant to help guide a student through the week's content and serve as a place to store review resources as well.

## Questions
The next/main/currently final section in each tutorial sheet are the problems. Each question has parts with answers and is categorized into question types. 

__Question types__ are titled with a level 2 heading (`##` in markdown), there are generaly three sections:
* Essential Questions
* Exam Style Questions
* Challenging Questions

__Questions__ are titled with a level 3 heading (`###`) and each __part__ is manually lettered such as: (a).

__Answers__ are contained within a html div with the class "answer" (`<div class = "answer"></div>`), this allows for dynamic collapse/expand.

Here is an example problem from the functions tutorial sheet:

```markdown
### Problem 1.
Separate the following using the method of partial fractions.

(a) $f(x) = x^3 e^{2x}$
<div class = "answer">$\Rightarrow{}$ Using product rule $\Rightarrow{} \frac{d}{dx}(uv) = v\frac{du}{dx} + u\frac{dv}{dx}\\ \Rightarrow{} u = x^3,\quad v=\exp{(2x)}$
$\Rightarrow{} \frac{du}{dx} = 3x^2$
$\Rightarrow{}$ using chain rule $\frac{d}{dx}v(g(x)) = \frac{dv}{dg}\frac{dg}{dx}$ to solve $\frac{dv}{dx}$ with $g(x) = 2x$
$\Rightarrow{} \frac{dv}{dx} = 2\exp{(2x)}$
$\Rightarrow{} \frac{df(x)}{dx} = 3x^2\exp{(2x)} + 2x^3\exp{(2x)}$
$\Rightarrow{} \boxed{\frac{df(x)}{dx} = x^2\exp{(2x)}(3 + 2x)}$
</div>
```

