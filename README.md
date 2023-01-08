# Spotify Image Generator
 
Generates personalized cover art based on user data.


## TABLE OF CONTENTS

* [Background](#background)
* [Objective](#objective)
* [Tools and Packages](#tools)
* [Model Implementation](#model-implementation)
* [Conclusion](#conclusion)
* [Challenges and Future Work](#challenges-and-futurework)

<hr>

## BACKGROUND 
Spotify defaults to a simple collage of four album covers as cover art for a playlist created by user. In order to change the playlist cover art, the user has to select and upload their personal images through their desktop Spotify application. In order to help this selection process, this project generates a completely new cover art based on the user's music preferences.

<hr>

## OBJECTIVE 
* Collect user data
  * Pull user data using Spotify API
  * Use Spotify API functions to specify queries
  * Parse through JSON format output to gather necessary data
* Test different image generator models
  * Find objects within cover art using TensorFlow object detection
  * Implement Artistic Style Transfer with TensorFlow Lite
  * Implement OpenAI's DALL·E2 model

<hr> 

## TOOLS
**Language Used:** Python
<table style="width:100%">
  <tr>
    <th>Task</th>
    <th>Technique</th> 
    <th>Tools/Packages Used</th>
  </tr>
  <tr>
    <td>Data Collection</td>
    <td>User top artists, artists' top song, top song's album, album's cover art data extraction through Spotify API</td> 
    <td>Spotify API (Spotipy)</td>
  </tr>
  <tr>
    <td>Data Pre-processing</td>
    <td>Sorted JSON output into lists</td> 
    <td>numpy</td>
  </tr>
  <tr>
    <td>Model Implementation</td>
    <td>Extracted objects within cover art using TensorFlow object detection. Implmented Artistic Style Transfer with TensorFlow Lite & OpenAI's DALL-E2 model to generate user-specific cover art.</td> 
    <td>TensorFlow, DALL·E 2</td>
  </tr>
</table><br>

## MODEL-IMPLEMENTATION

<h3>Spotify API Connection</h3>
(Authenticate user's Spotify account) <br>
↓
<h3>Spotipy Queries</h3>
(Extract and store as lists: User's top artists → artist's top song → album that the top song belongs to → cover art for each album) <br>
↓
<h3>Test Artistic Style Transfer with TensorFlow Lite</h3>
(Pull sample cover arts using Spotipy and demonstrate Artistic Style Transfer implementation and functionality) <br>
↓
<h3>TensorFlow object detection</h3>
(Find prevelant objects within selected top cover art using object detection. Store output into lists.) <br>
↓
<h3>OpenAI's DALL·E 2 model</h3>
(Use object output list from above step to generate a sentence/prompt for the DALL·E 2 model to process.)
↓
<h3>Apply Artistic Style Transfer with TensorFlow Lite</h3>
(Run the DALL·E 2 output image through Artistic Style Transfer model to generate final image) <br>

## CONCLUSION 

Although the end result of the models did not succeed in creating what we may consider 'artistic' or 'stylistic' art, this project set up a scalable framework for future improvement and also demonstrated the power and relative simplicity of recent development in image generation using deep learning.

<hr>


## CHALLENGES-AND-FUTUREWORK 

* Extract genres for each song/album that was fed into the model, and use adjectives associated with the genre or song/album title as part of the prompt for the DALL·E 2 model. This may provide more context for the model to work with and may produce a greater variety as output.
