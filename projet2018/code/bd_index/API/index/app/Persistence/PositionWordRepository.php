<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:08
 */
namespace App\Persistence;
use App\Repositories\Repository;
use Illuminate\Support\Facades\DB;

class PositionWordRepository extends Repository
{
    public function store($data) {
        try {
            // Store in DB the data given
            DB::select('CALL PPOSITION_WORD(?,?,?,?,?,?,?,?)',array(
                $data['position'],
                $data['title'],
                $data['word'],
                $data['type_entity'],
                $data['pos_tag'],
                $data['id_article'],
                $data['file_wiki'],
                $data['synonym']
            ));

            $this->response['message'] = "";
            $this->response['code'] =  Repository::$CREATION_SUCCEEDED;

            return $this->response;
        } catch (\PDOException $e) {
            // Get the pdo exception message
            $this->response['message'] = $e->getMessage();
            $this->response['code'] =  Repository::$INTERNAL_ERROR;

            return $this->response;
        }
    }
}