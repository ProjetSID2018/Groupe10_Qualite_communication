<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 09/01/2018
 * Time: 10:35
 */

namespace App\Persistence;



use App\Repositories\Repository;
use Illuminate\Support\Facades\DB;

class WikiRepository extends Repository
{
    public function store($data) {
        try {
            // Store in DB the data given
            DB::select('CALL PWIKI(?,@id_wiki)',array(
                $data['file_wiki'],
            ));

            // Get the output variable from the procedure
            $results = DB::select('Select @id_wiki as id_wiki');

            // Sent the id_wiki in json format to client
            $this->response['message'] = ['id_wiki' =>$results[0]->id_wiki];
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