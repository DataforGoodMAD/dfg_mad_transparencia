# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from db.database import create_db_and_tables, engine, get_db_session
from models.departamento import Departamento
from models.diario import Diario
from models.disposicion_boe import DisposicionBOE
from models.estado_consolidacion import EstadoConsolidacion
from models.estatus_legislativo import EstatusLegislativo
from models.origen_legislativo import OrigenLegislativo
from models.rango import Rango
from models.seccion import Seccion
from models.subseccion import Subseccion

# Load database metadata before running any pipeline
create_db_and_tables(engine=engine)


class SaveToDBItemPipeline:
    def process_item(self, item, spider):
        with get_db_session() as session:
            session.add(item)
            session.commit()
