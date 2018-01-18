<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:05
 */
namespace App\Persistence;
use App\Repositories\Repository;
use Illuminate\Support\Facades\DB;

class AuthorRepository extends Repository
{
    public function store($data) {
        try {
            // Store in DB the data given
            DB::select('CALL PAUTHOR(?,?,?)',array(
                $data['id_article'],
                $data['surname_author'],
                $data['firstname_author'],
            ));

            // Get the output variable from the procedure
            $results = DB::select('Select @id_author as id_author');

            // Sent the id_author in json format to client
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