<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:11
 */
namespace App\Services;

use App\Persistence\WordRepository;

class WordService
{
    private $word_repository;
    public function __construct()
    {
        $this->word_repository = new WordRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->word_repository->store($data);
    }
}