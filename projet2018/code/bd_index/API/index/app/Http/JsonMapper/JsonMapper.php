<?php
/**
 * Created by PhpStorm.
 * User: William AZZOUZA
 * Date: 08/01/2018
 * Time: 13:57
 * Groupe 2 (Index)
 */
namespace App\Http\JsonMapper;


class JsonMapper
{

    /**
     * Allow to parse the json and to put in an array the key
     * and the value corresponding
     * @param $request_array
     * @return array
     */
    public function json_mapper($request_array)
    {
        $data = array();
        foreach ($request_array as $key => $value) {
            $data[$key] = $value;
        }
        return $data;
    }
}