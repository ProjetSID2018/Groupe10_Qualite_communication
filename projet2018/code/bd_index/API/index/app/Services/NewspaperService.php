<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:10
 */
namespace App\Services;

use App\Persistence\NewspaperRepository;

class NewspaperService
{
    private $newspaper_repository;
    public function __construct()
    {
        $this->newspaper_repository = new NewspaperRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->newspaper_repository->store($data);
    }

}