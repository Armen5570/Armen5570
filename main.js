
const world = Globe()
  (document.getElementById("globe"))
  .globeImageUrl(
    "https://unpkg.com/three-globe/example/img/earth-blue-marble.jpg"
  )
  .backgroundColor("#020817")
  .showAtmosphere(true)
  .atmosphereColor("#168cff")
  .atmosphereAltitude(0.2)
  .pointsData([
    { lat: 40.18, lng: 44.51, size: 0.7 },
    { lat: 51.50, lng: -0.12, size: 0.5 },
    { lat: 40.71, lng: -74.00, size: 0.5 },
    { lat: 35.68, lng: 139.69, size: 0.5 },
    { lat: 28.61, lng: 77.20, size: 0.5 },
    { lat: -33.86, lng: 151.20, size: 0.5 },
    { lat: -23.55, lng: -46.63, size: 0.5 }
  ])
  .pointColor(() => "#00eaff")
  .pointAltitude(0.02)
  .pointRadius(d => d.size)
  .arcsData([
    { startLat: 40.18, startLng: 44.51, endLat: 51.50, endLng: -0.12 },
    { startLat: 40.18, startLng: 44.51, endLat: 40.71, endLng: -74.00 },
    { startLat: 40.18, startLng: 44.51, endLat: 35.68, endLng: 139.69 },
    { startLat: 40.18, startLng: 44.51, endLat: 28.61, endLng: 77.20 },
    { startLat: 40.18, startLng: 44.51, endLat: -33.86, endLng: 151.20 },
    { startLat: 40.18, startLng: 44.51, endLat: -23.55, endLng: -46.63 }
  ])
  .arcColor(() => ["#00eaff", "#187bff"])
  .arcDashLength(0.4)
  .arcDashGap(0.2)
  .arcDashAnimateTime(1800)
  .arcStroke(0.6);

world.controls().autoRotate = true;
world.controls().autoRotateSpeed = 0.5;
world.controls().enableDamping = true;

window.addEventListener("resize", () => {
  world.width(window.innerWidth);
  world.height(window.innerHeight);
});
