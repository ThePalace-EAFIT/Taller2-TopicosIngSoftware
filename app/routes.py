import os, random
from flask import Blueprint, jsonify, render_template, current_app
from .models import POKENEAS
from .services.s3 import build_public_url

bp = Blueprint("core", __name__)

def _container_id() -> str:
    return os.getenv("HOSTNAME", "local")

@bp.route("/api/pokenea")
def api_pokenea():
    pok = random.choice(POKENEAS)
    data = {
        "id": pok["id"],
        "nombre": pok["nombre"],
        "altura_m": pok["altura_m"],
        "habilidad": pok["habilidad"],
        "container_id": _container_id()
    }
    return jsonify(data)

@bp.get("/imagen")
def imagen():
    pok = random.choice(POKENEAS)
    bucket = current_app.config["S3_BUCKET"]
    region = current_app.config["AWS_REGION"]
    img_url = build_public_url(bucket, region, pok["imagen_key"])
    return render_template(
        "imagen.html",
        nombre=pok["nombre"],
        frase=pok["frase"],
        img_url=img_url,
        container_id=_container_id()
    )