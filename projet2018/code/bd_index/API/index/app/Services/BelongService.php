<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 09/01/2018
 * Time: 14:40
 */
namespace App\Services;

use App\Persistence\BelongRepository;

class BelongService
{
    private $belong_repository;
    public function __construct()
    {
        $this->belong_repository = new BelongRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->belong_repository->store($data);
    }
}