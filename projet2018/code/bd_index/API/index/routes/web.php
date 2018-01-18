<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
*/
Route::prefix('var/www/html/projet2018/code/bd_index/API/index')->group(function () {
    // Entity's routes
    Route::post('entity', 'EntityController@store');

    // Newspaper's routes
    Route::post('newspaper', 'NewspaperController@store');

    // Word's routes
    Route::post('word', 'WordController@store');

    // Word_Position's routes
    Route::post('positionword', 'PositionWordController@store');

    // Synonym's routes
    Route::post('synonym', 'SynonymController@store');

    // Wiki's routes
    Route::post('wiki', 'WikiController@store');

    // Label's routes
    Route::post('label', 'LabelController@store');

    // Pos_Tagging's routes
    Route::post('postagging', 'PosTaggingController@store');

    // Belong's routes
    Route::post('belong', 'BelongController@store');

    // Article's routes
    Route::post('article', 'ArticleController@store');
});

