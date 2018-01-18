<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:10
 */
namespace App\Services;

use App\Persistence\PosTaggingRepository;

class PosTaggingService
{
    private $post_tagging_repository;
    public function __construct()
    {
        $this->post_tagging_repository = new PosTaggingRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->post_tagging_repository->store($data);
    }
}