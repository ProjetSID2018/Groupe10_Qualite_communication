<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:11
 */
namespace App\Services;

use App\Persistence\SynonymRepository;

class SynonymService
{
    private $synonym_repository;
    public function __construct()
    {
        $this->synonym_repository = new SynonymRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->synonym_repository->store($data);
    }
}