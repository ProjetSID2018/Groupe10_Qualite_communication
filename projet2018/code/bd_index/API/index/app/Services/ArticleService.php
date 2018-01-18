<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:09
 */
namespace App\Services;

use App\Persistence\ArticleRepository;

class ArticleService
{
    private $article_repository;
    public function __construct()
    {
        $this->article_repository = new ArticleRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->article_repository->store($data);
    }
}