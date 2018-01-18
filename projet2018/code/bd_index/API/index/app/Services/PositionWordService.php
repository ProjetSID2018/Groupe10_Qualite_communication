<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:10
 */
namespace App\Services;

use App\Persistence\PositionWordRepository;

class PositionWordService
{
    private $position_word_repository;
    public function __construct()
    {
        $this->position_word_repository = new PositionWordRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->position_word_repository->store($data);
    }
}