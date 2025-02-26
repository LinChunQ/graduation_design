def model_to_dict(model_instance):
    """将 SQLAlchemy 实体转换为字典（适用于任意模型）"""
    return {column.name: getattr(model_instance, column.name) for column in model_instance.__table__.columns}
