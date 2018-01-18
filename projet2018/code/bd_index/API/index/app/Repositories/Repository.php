<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 09/01/2018
 * Time: 21:05
 */

namespace App\Repositories;


abstract class Repository implements RepositoryInterface
{
    /* An array containing the response that will be send to client */
    protected $response = array();

    /* If the creation is a succeed, we send this status code */
    protected static $CREATION_SUCCEEDED = 201;

    /* If there is any internal problems, we send this status code */
    protected  static $INTERNAL_ERROR = 500;

    /* Function that allows us to store data in our database, according to an existing table */
    public abstract function store($data);

}