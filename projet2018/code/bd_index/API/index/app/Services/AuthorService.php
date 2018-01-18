<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:09
 */
namespace App\Services;

use App\Persistence\AuthorRepository;

class AuthorService
{
    private $author_repository;
    public function __construct()
    {
        $this->author_repository = new AuthorRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->author_repository->store($data);
    }
}