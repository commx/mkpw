class Mkpw < Formula
  desc "mkpw is a small tool to generate safe passwords"
  homepage "https://github.com/commx/mkpw"
  url "https://github.com/commx/mkpw/archive/0.1.1.tar.gz"
  version "0.1.1"
  sha256 "b1f6b823427eee5cc5dbd09724aa0bed3ac6d33e59108a2cc52698a254279df6"

  def install
    bin.install "mkpw"
    man8.install "mkpw.8"
  end

  test do
    system "#{bin}/mkpw", "1"
  end
end
