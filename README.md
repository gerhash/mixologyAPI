
# Mixology API - Cocktail's Api with tutorial & story
<img src="https://skillicons.dev/icons?i=py,flask,html,css,js,bootstrap" alt="Skills" />

## Overview
This API provides detailed information about cocktails. Each cocktail entry includes essential details such as its ID, name, image URL, ingredients list with quantities and measurement units, a step-by-step preparation tutorial, a historical background of the cocktail, and the difficulty level of making it.

## Purpose
The purpose of this API is to provide users with comprehensive information about various cocktails. By using this API, users can discover new cocktail recipes, learn about the history behind each drink, understand the necessary ingredients and their quantities, and follow detailed preparation instructions. This API is ideal for bartenders, cocktail enthusiasts, and anyone looking to expand their knowledge and skills in cocktail making. It serves as a valuable resource for both novice and experienced mixologists, promoting the art of cocktail crafting and enhancing the overall cocktail experience.

## Usage

#### domain.com/{api_call}

# GET

## /cocktails
This endpoint retrieves a list of all available cocktails.

## /cocktails/{cocktail-id}
This endpoint retrieves a specific cocktail by its ID

## /cocktails/search_by_name?={name}
This endpoint retrieves cocktails that match a specified name query (case-insensitive).

## /cocktails/search?={ingredient1},{ingredient2}
This endpoint retrieves cocktails that contain all specified ingredients.

## /cocktails/difficulty/{difficulty}
This endpoint retrieves cocktails that match the specified difficulty level.


