<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 17:56
 */

namespace App\Http\Controllers;


use App\Http\JsonMapper\JsonMapper;
use App\Services\SynonymService;
use Illuminate\Http\Request;

class SynonymController extends Controller
{

    private $json_mapper;
    private $synonym_service;

    public function __construct()
    {
        $this->json_mapper = new JsonMapper();
        $this->synonym_service = new SynonymService();
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        // Parse automatically the json sent by client
        $raw_data = $this->json_mapper->json_mapper($request->all());

        // Return the appropriate message to client
        return $this->parse($raw_data,$this->synonym_service);
    }
}