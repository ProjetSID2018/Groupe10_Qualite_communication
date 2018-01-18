<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 09/01/2018
 * Time: 21:10
 */

namespace App\Repositories;


interface RepositoryInterface
{
    /**
     * Allow to store data in the concerned table
     * @param $data :an array containing all the data parse
     * from the json sent by client
     * @return :a response that will be interpreted by client
     */
    public function store($data);

}