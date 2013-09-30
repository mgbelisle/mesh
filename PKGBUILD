pkgname=mesh
pkgver=0.0.1
pkgrel=1
pkgdesc='Quick mesh network setup'
url="https://github.com/mgbelisle/${pkgname}"
license=('MIT')
arch=('any')
depends=('python' 'iw' 'batctl' 'avahi' 'nss-mdns')
backup=('etc/mesh.conf')

package() {
  cp -r * "${pkgdir}"
}
