from app import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment='主键')
    userAccount = db.Column(db.String(256), unique=True, nullable=False, comment='用户账号')
    userName = db.Column(db.String(256), comment='昵称', nullable=False)
    userPassword = db.Column(db.String(512), nullable=False, comment='密码')
    userProfile = db.Column(db.String(512), comment='用户简介')
    userRole = db.Column(db.String(256), default=0, comment='用户角色：user/admin')
    userAvatar = db.Column(db.String(1024), comment='用户头像')
    createTime = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    updateTime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False, comment='更新时间')
    editTime = db.Column(db.DateTime, comment='编辑时间')
    isDelete = db.Column(db.SmallInteger, default=0, nullable=False, comment='是否删除')

    def __init__(self, userAccount,userPassword,userName='无名',userProfile=None,userRole='user',userAvatar=None):
        self.userAccount = userAccount
        self.userName = userName
        self.userPassword = userPassword
        self.userProfile = userProfile
        self.userRole = userRole
        self.userAvatar = userAvatar
        self.createTime = datetime.now()
        self.editTime = datetime.now()
        self.updateTime = datetime.now()
        self.isDelete = 0   
    
    def __getitem__(self, key):
        return getattr(self, key)