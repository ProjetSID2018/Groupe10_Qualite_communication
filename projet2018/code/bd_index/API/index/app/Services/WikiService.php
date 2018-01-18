<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 09/01/2018
 * Time: 10:35
 */
namespace App\Services;

use App\Persistence\WikiRepository;

class WikiService
{
    private $wiki_repository;
    public function __construct()
    {
        $this->wiki_repository = new WikiRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->wiki_repository->store($data);
    }
}