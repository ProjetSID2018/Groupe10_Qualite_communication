        var datatest=[
    {
        "source": "figaro",
        "nombre" : 210
    },
    {
        "source": "monde",
        "nombre": 2015
    },
    {
        "source": "depeche",
        "nombre" : 50
    },
    {
        "source": "set",
        "nombre": 45
    },
    {
        "source": "truc",
        "nombre" : 544
    },
    {
        "source": "ouai",
        "nombre": 45
    },
    {
        "source": "plus",
        "nombre" : 76
    },
    {
        "source": "trente",
        "nombre": 71
    },
    {
        "source": "aller",
        "nombre" : 828
    },
    {
        "source": "test",
        "nombre": 783
    }
]
/*
function start(){

    request_top_10()
}

function request_top_10(){
    $('#top10_sources').hide();
    drawBasic()
    $.ajax({
        url:'http//localhost:5000/',
        type: 'POST',
        dataType: 'json',
        sucess: drawBasic,
        error: ajax_failed,
    });
}
*/

google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBasic);

function drawBasic() {

      $('#top10_sources').show();
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'sources');
      data.addColumn('number', "nombres d'articles");

      for (var i = 0; i <10; i++) {
        data.addRow([datatest[i].source,datatest[i].nombre ]);
      }

      var options = {
        hAxis: {
          title: 'sources',
          format: 'string',
        },
        vAxis: {
          title: "nombres d'articles par source"
        }
      };

      var chart = new google.visualization.ColumnChart(
        document.getElementById('chart_div'));

      chart.draw(data, options);

    }


    function ajax_failed(){
        alert('erreur');
        alert(result);
    }
