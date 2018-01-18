<?php

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class EntityProcedures extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        DB::unprepared('
    CREATE PROCEDURE PENTITE1(IN arg_type_entite INT)
    BEGIN
        INSERT INTO entite(type_entite) VALUES (arg_type_entite);
    END'
        );

        DB::unprepared('
    CREATE PROCEDURE PENTITE2(IN arg_type_entite INT)
    BEGIN
        INSERT INTO entite(type_entite) VALUES (arg_type_entite);
    END'
        );

        DB::unprepared('
    CREATE PROCEDURE PENTITE3(IN arg_type_entite INT)
    BEGIN
        INSERT INTO entite(type_entite) VALUES (arg_type_entite);
    END'
        );
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        //
    }
}
