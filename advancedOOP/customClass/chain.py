
#实现		GET /users/:user/repos
class Chain(object):
	def __init__(self='', path=''):
		self._path = path;
	def __getattr__(self, attr):
		if attr == 'users':
			return lambda name: Chain('%s/%s' % (self._path, 'users/'+name)) 
		return Chain('%s/%s' % (self._path, attr))
	def __str__(self):
		return self._path;

	__repr__ = __str__

print(Chain('face-manage').api.weixin.staff.list)
print(Chain('face-manage').api.users('xcleung').gg)

