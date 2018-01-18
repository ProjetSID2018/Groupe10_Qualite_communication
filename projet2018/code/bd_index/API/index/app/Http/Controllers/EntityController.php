<?php

namespace App\Http\Controllers;

use App\Http\JsonMapper\JsonMapper;
use App\Services\EntityService;
use Illuminate\Http\Request;

class EntityController extends Controller
{

   private $json_mapper;
   private $entity_service;

    public function __construct()
    {
        $this->json_mapper = new JsonMapper();
        $this->entity_service = new EntityService();
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
        return $this->parse($raw_data,$this->entity_service);
    }


}
