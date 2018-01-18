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

class WordRepository extends Repository
{
    public function store($data) {
        try {
            // Store in DB the data given
            DB::select('CALL PWORD(?,?,@id_word)',array(
                $data['word'],
                $data['lemma'],
            ));

            // Get the output variable from the procedure
            $results = DB::select('Select @id_word as id_word');

            // Sent the id_word in json format to client
            $this->response['message'] = ['id_word' =>$results[0]->id_word];
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