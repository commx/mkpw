class Mkpw < Formula
  desc "mkpw is a small tool to generate safe passwords"
  homepage "https://github.com/commx/mkpw"
  url "https://github.com/commx/mkpw/archive/0.2.0.tar.gz"
  version "0.2.0"
  sha256 "1bdf2023da767ac5f1735b7c4a2e3d1854eb0bedf6df72ce10c380567d7cd85e"

  def install
    bin.install "mkpw"
  end

  test do
    system "#{bin}/mkpw", "1"
  end
end
