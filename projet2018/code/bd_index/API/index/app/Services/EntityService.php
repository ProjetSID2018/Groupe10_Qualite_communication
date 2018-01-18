<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:10
 */
namespace App\Services;

use App\Persistence\EntityRepository;

class EntityService
{
    private $entity_repository;
    public function __construct()
    {
        $this->entity_repository = new EntityRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->entity_repository->store($data);
    }

}