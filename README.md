<!---Note: Although this is a markdown file, this specific README.md file is written for the GitHub markdown interpreter, not the Obsidian Md interpreter. As a result, this page may not be displayed correctly in Obsidian Md. Don't worry, this is fine, as this page is not part of the companion.    ---> 

# AE4874-Companion
An Obsidian Md vault containing a study companion / summary for the AE4874 Astrodynamics course.

The contents of this repo are an [Obsidian Md](https://obsidian.md/) vault, which is a collection of interconnected markdown (.md) files. This creates a network of readable information that acts much like a local Wiki, or a web-book. In the terminology of Obsidian Md, such a collection of markdown files is called a **vault**.
___
## Progress

| Topic         | Progress      |
| ------------- |:-------------:|
| Basic concepts | ![text](https://progress-bar.dev/100) |
| N-body problem    | ![text](https://progress-bar.dev/100) |
| Two-body problem    | ![text](https://progress-bar.dev/70) |
| Three-body problem | ![text](https://progress-bar.dev/20) |
| Standards of space and time | ![text](https://progress-bar.dev/0) |
| Orbital transfers    | ![text](https://progress-bar.dev/15) |
| Solar system transfers   | ![text](https://progress-bar.dev/5) |
| Relative satellite motion | ![text](https://progress-bar.dev/15) |
| Exercises | ![text](https://progress-bar.dev/5) |


___
## Quick start guide
1. **Install Obsidian Md** from the [download webpage](https://obsidian.md/download). It is available for Linux, Windows, and MacOS. This quick start guide will assume you are using Linux. 
   I recommend installing either the .deb or .tar.gz, but there are flatpak and Snap store versions available too. There is currently no way to install using `apt`.
2. **Download this repository**. You can download it as a .zip file with the button above, or clone from the command line interface using
```md
git clone https://github.com/Hans-Bananendans/Astrodynamics-Companion.git
```
or
```md
gh repo clone Hans-Bananendans/Astrodynamics-Companion
```
(this command requires the [GitHub CLI](https://cli.github.com/) to be installed)

3. Open Obsidian Md, open a vault and select the option *Open folder as vault*. Select the folder in which you cloned this repository as the vault location. If successful, you will see a list of the files in this repository appear in a column on the left-hand side.
![installation2.png](./media/installation2.png)

4. This companion uses numerous custom information boxes, attached as a CSS snippet. It is recommended you enable these, at it makes the document **much** more readable.
	1. Go to **Options** -> **Appearance** -> **CSS Snippets**
	2. Enable the checkbox on *custom_callouts*
5. (OPTIONAL) Obsidian Md can be expanded using an increasingly large pool of community-made plugins. These plugins cannot be validated by the Obsidian Md developers, and so they disable the use of these plugins by default. Don't worry, this repository only uses two plugins, both of which are open-source and safe for use.
	1. Go to **Options** -> **Community plugins** and turn Safe mode OFF.
	2. If you plan on going through some of the code examples, it is recommended to install the [Editor Syntax Highlight](https://github.com/deathau/cm-editor-syntax-highlight-obsidian) plugin. This will make it easier to read the code snippets contained in the companion.
	3. If you also plan to help expand this companion, I recommend you also install [Paste to Current Indentation](https://github.com/jglev/obsidian-paste-to-current-indentation) because this makes pasting text and code into callout boxes much less painful.
<!-- If you went through the optional steps, the Community Plugin tab in the Option panel should look like this:
 ![installation1.png](./media/installation1.png) -->

And that's it, you should now be good to go
___

## Dark mode
This companion is set up in such a way that **it does not matter whether you use light or dark mode**. All the figures use colours and shades that have enough contrast to see on light or dark backgrounds. My preference is to use dark mode, as it is easier on the eyes at night, but feel free to take your pick.

![installation3.png](./media/installation3.png)

___
## Using this companion
You are free to use this companion however suits you best. However, to use it as a proper "companion" to the material of the AE4874 course, you would do best to use the index in the `_INDEX_.md` file, which is also the recommended reading order. Not only does this reading order follow the structure of the lecture syllabus, it is also roughly the order in which the sections will be written, so that will likely be the most natural way to read it.

In addition, you can use the index or Obsidian's search function to search the whole vault for topics or keywords.

___
## Contribution
If you are a fellow student and would like to contribute to this guide, feel free to contact me. Alternatively, you can clone the `development` branch and submit a pull request. Much appreciated! :heart:

___
## Dependencies
This Obsidian vault uses the following community plugins:
 - [Editor Syntax Highlight](https://github.com/deathau/cm-editor-syntax-highlight-obsidian)
