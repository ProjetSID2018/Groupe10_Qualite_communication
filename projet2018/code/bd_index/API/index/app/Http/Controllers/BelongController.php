<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 09/01/2018
 * Time: 14:39
 */

namespace App\Http\Controllers;


use App\Http\JsonMapper\JsonMapper;
use App\Services\BelongService;
use Illuminate\Http\Request;

class BelongController extends Controller
{
    private $json_mapper;
    private $belong_service;

    public function __construct()
    {
        $this->json_mapper = new JsonMapper();
        $this->belong_service = new BelongService();
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
        return $this->parse($raw_data,$this->belong_service);
    }

}